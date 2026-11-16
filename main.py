import speedtest
import subprocess
import platform
import re
import statistics
from colorama import init, Fore

init(autoreset=True)


def print_header():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "          PYTHON NETWORK SPEED TEST")
    print(Fore.CYAN + "=" * 50)


def measure_jitter(host="1.1.1.1", samples=5):
    ping_times = []

    system = platform.system().lower()

    for _ in range(samples):
        try:
            if system == "windows":
                result = subprocess.run(
                    ["ping", "-n", "1", "-w", "2000", host],
                    capture_output=True,
                    text=True
                )
            else:
                result = subprocess.run(
                    ["ping", "-c", "1", "-W", "2", host],
                    capture_output=True,
                    text=True
                )

            match = re.search(
                r"time[=<]([\d.]+)\s*ms",
                result.stdout,
                re.IGNORECASE
            )

            if match:
                ping_times.append(float(match.group(1)))

        except Exception:
            continue

    if len(ping_times) < 2:
        return None

    differences = [
        abs(ping_times[i] - ping_times[i - 1])
        for i in range(1, len(ping_times))
    ]

    return statistics.mean(differences)


def run_speed_test():
    print_header()

    try:
        print(Fore.YELLOW + "\nInitializing speed test...")

        test = speedtest.Speedtest()

        print(Fore.YELLOW + "Finding the best server...")

        test.get_best_server()

        server = test.results.server

        print(Fore.GREEN + "\n[ SERVER INFORMATION ]")
        print(f"Server Name : {server['name']}")
        print(f"Country     : {server['country']}")
        print(f"ISP         : {test.results.client['isp']}")

        print(Fore.YELLOW + "\nTesting download speed...")

        download = test.download() / 1_000_000

        print(Fore.YELLOW + "Testing upload speed...")

        upload = test.upload() / 1_000_000

        ping = test.results.ping

        print(Fore.YELLOW + "Measuring network jitter...")

        jitter = measure_jitter()

        print(Fore.GREEN + "\n[ TEST RESULTS ]")

        print(f"Download : {download:.2f} Mbps")
        print(f"Upload   : {upload:.2f} Mbps")
        print(f"Ping     : {ping:.2f} ms")

        if jitter is not None:
            print(f"Jitter   : {jitter:.2f} ms")
        else:
            print("Jitter   : Unable to measure")

        print(Fore.CYAN + "\n" + "=" * 50)
        print(Fore.GREEN + "       SPEED TEST COMPLETED!")
        print(Fore.CYAN + "=" * 50)

    except Exception as error:
        print(Fore.RED + f"\nError: {error}")
        print(Fore.YELLOW + "Please check your internet connection.")


if __name__ == "__main__":
    run_speed_test()