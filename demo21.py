from common.const import MAX_CONCURRENT_JOBS
import common.const

print(MAX_CONCURRENT_JOBS, common.const.MAX_CONCURRENT_JOBS)
print("begin", hex(id(MAX_CONCURRENT_JOBS)), hex(id(common.const.MAX_CONCURRENT_JOBS)))
MAX_CONCURRENT_JOBS -= 100
print(MAX_CONCURRENT_JOBS, common.const.MAX_CONCURRENT_JOBS)
print("after", hex(id(MAX_CONCURRENT_JOBS)), hex(id(common.const.MAX_CONCURRENT_JOBS)))
