
import os
from hfipcheck import check_ip

TEST_DIR = "test_ips"

def run_tests():
    for filename in os.listdir("."):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(".", filename)
        print(f"\nRunning tests from: {filename}")
        with open(filepath, "r") as f:
            for line in f:
                ip = line.strip()
                if ip:
                    result = check_ip(ip)
                    print(f"{ip} → {result}")
            print("\n")
if __name__ == "__main__":
    run_tests()
