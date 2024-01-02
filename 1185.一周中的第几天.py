import calendar

if __name__ == '__main__':
    '''
    day = 31
    month = 8
    year = 2019
    '''
    day = 31
    month = 8
    year = 2019
    weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # 步骤1：定义每周7天
    c = calendar.monthrange(year=year, month=month)
    # 步骤2：调用calendar.monthrange(year,month)函数，返回两个整数。第一个是该月的第一天是星期几，第二个是该月有几天。
    print('firstday:', weekday[(c[0] + 1) % 7])
    # 假如c[0]：0则表示星期一，c[0]:6则表示星期日，加上%7防止超出数组索引范围，因此用weekday[(c[0] + 1) % 7]表示该月第一天是周几
    n = day - 1
    print('ans:', weekday[(c[0] + 1 + n) % 7])
    # 步骤3：计算参数day和第一天相隔的天数n，从c[0]+1下标依次右移n次，加上%7防止超出数组索引范围

    # 简化后的代码如下：
    '''
    import calendar


    class Solution:
        def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
            weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            c = calendar.monthrange(year=year, month=month)
            return weekday[(c[0] + day) % 7]
    '''
    
