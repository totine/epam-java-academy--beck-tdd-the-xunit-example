from xunit.xunit import WasRun

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)

