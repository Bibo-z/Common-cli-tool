import argparse
from .cli import main
from common.cli import run_diag

parser = argparse.ArgumentParser(description="Common CLI Tool – Ports, IP, Diag and More")

parser.add_argument("-p", "--ports", action="store_true", help="Show common ports")
parser.add_argument("-cmd", "--commands", action="store_true", help="Show network troubleshooting commands")
parser.add_argument("-calc", "--calculator", type=str, metavar="CIDR", help="IP calculator with CIDR (e.g., 192.168.0.1/24)")
parser.add_argument("-diag", action="store_true", help="Run basic system diagnostics")

args = parser.parse_args()  # ✅ Parse args first

if args.diag:
    run_diag()  # ✅ Correct and safe


main()
