from datetime import datetime


gettm = datetime.now

def fmt_tm(tm, pattern="%H:%M:%S"):
  return tm.strftime(pattern)

def note_time(func, *args):
  start = gettm()
  print(f"start: {fmt_tm(start)}")

  func(*args)

  end = gettm()
  print(f"end: {fmt_tm(end)}")

  print('diff:', end-start)


if __name__ == '__main__':
  note_time(lambda:0)
