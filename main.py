from testConfig import TestConfig
from trafficFlowTests import TrafficFlowTests
import arguments
import sys


def main():
    args = arguments.parse_args()
    cc = TestConfig(args.config)
    tft = TrafficFlowTests(cc)

    results = []
    for test in tft._cc.GetConfig():
        tft.run(test, args.evaluator_config)

        
        if not tft.evaluate_run_success():
            print(f"Failure detected in {test['name']} results")
            sys.exit(-1)

if __name__ == "__main__":
    main()
