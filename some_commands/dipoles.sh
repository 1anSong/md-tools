#工作流程
#在文件目录 001-1m-ffs/4-run; 002-2m-efc/4-run/; ... 010/4-run 执行命令
#需要执行gmx dipoles 
#然后屏幕上等待输入0
	for i in {001..010}*;do cd $i/4-run; echo -e "0 \n"|gmx dipoles;cd ../..;done > dipoles_xcsong
