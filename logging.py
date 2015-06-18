


"""
This advice comes from http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python

Capture exceptions and record them with traceback

It is always a good practice to record when something goes wrong, but it won’t be helpful if there is no traceback. You should capture exceptions and record them with traceback. Following is an example:

try:
    open('/path/to/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception, e:
    logger.error('Failed to open file', exc_info=True)

By calling logger methods with exc_info=True parameter, traceback is dumped to the logger. As you can see the result

ERROR:__main__:Failed to open file
Traceback (most recent call last):
  File "example.py", line 6, in <module>
    open('/path/to/does/not/exist', 'rb')
IOError: [Errno 2] No such file or directory: '/path/to/does/not/exist'

You can also call logger.exception(msg, *args), it equals to logger.error(msg, exc_info=True, *args).

"""

