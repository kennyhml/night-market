from licensing.models import *
from licensing.methods import Key, Helpers
import json

RSAPubKey = "<RSAKeyValue><Modulus>lq+AOf4UYoJAH4w3qXm5LzH0dHRzH+pOOE4DPF2GY3SmlVSOufiXhuVlaKMeoxwkNrmn6vT4GcnvphpzGwDVE+4RKT/NP8hFw3h9mewohpAKCkNymLhSV2dIsU2RAnexVc51HfrEjsmmJzXUV71h8gaEypt0rZ6utwsTaJ0sZUsw9uUfF0ouiCe+tObxOEnvOLcvygjHtlHyBHIPLTVipwHv790PFz7UL1MRGWCB92t6+F4GuP0XV5FuQLgslIPL1ar1SzrFc8+PHMWbhH2UobJ0emzt40WAWDKK5r3lUzBwNvvdCd2QmsoEh6ttWQaarBsfvvrgVVhds63XcKO4KQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyIxNjAzODU1MSIsImFlVnh2c1hMRDhLeTlTd0dlVHE3YzZMcG1FRlV6MmYzdUdMaDJ6Yk8iXQ=="
product_id = 16631


def check_key_valid_hwid():
    """
    Takes the key from json and checks if its valid.\n
    Returns valid-bool and the subscription-version.
    """
    with open("data\Settings.json", "r") as json_file:
        config = json.load(json_file)

    try:
        valid = Key.activate(
            token=auth,
            rsa_pub_key=RSAPubKey,
            product_id=product_id,
            key=config["key"],
            machine_code=Helpers.GetMachineCode(),
        )
        if valid[0]:
            with open("archive/licensefile.skm", "w") as f:
                f.write(valid[0].save_as_string())
            return True
        print(f"License is not valid: {valid[1]}")

    except Exception as e:
        print(e)
        print(
            "Woooops! Looks like youre computer does not like HWIDs."
            "Lets try your MAC address instead! :)"
        )
        return check_key_valid_mac()


def check_key_valid_mac():
    """
    For some people the hwid seems to be bugged or spoofed.
    This will use the mac address instead.
    """
    with open("dat\Settings.json", "r") as json_file:
        config = json.load(json_file)

    try:
        valid = Key.activate(
            token=auth,
            rsa_pub_key=RSAPubKey,
            product_id=product_id,
            key=config["key"],
            machine_code=Helpers.GetMACAddress(),
        )
        if valid[0]:
            with open("archive/licensefile.skm", "w") as f:
                f.write(valid[0].save_as_string())
            return True
        print(f"License is not valid: {valid[1]}")

    except Exception as e:
        print(e)
        print(
            "Wow, looks like you stole your computer from NASA or something else isnt right!"
            "Please contact the support!"
        )
        return None


def get_data():
    with open("archive/licensefile.skm", "r") as f:
        ls = LicenseKey.load_from_string(RSAPubKey, f.read())
        if not ls.customer["Name"]:
            ls.customer["Name"] = "Unknown"

    return {
        "device_limit": (int(len(ls.activated_machines)), int(ls.max_no_of_machines)),
        "customer_name": ls.customer["Name"],
        "first_login": ls.created,
        "expires": str(ls.expires),
    }
