start_num = int(10)
end_num = int(150)
cnt = start_num
while cnt <= end_num:
	if cnt % 15 == 0 and cnt % 5 == 0:
		print(cnt)
	cnt += 1