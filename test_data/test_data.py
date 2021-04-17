success_data = {'name': '登录功能-正常登录', 'username': '18275366410', 'password': 'lqh18275366'}
failed_data = [
    {'name': '登录功能-异常登录-用户名为空', 'username': '', 'password': '654321','error_msg':'用户名不能为空'},
    {'name': '登录功能-异常登录-用户名错误', 'username': 'abc', 'password': 'lqh18276366','error_msg':'账号或密码错误'},
    {'name': '登录功能-异常登录-密码为空', 'username': '18275366410', 'password': '','error_msg':'密码不能为空'},
    {'name': '登录功能-异常登录-密码错误', 'username': '18275366410', 'password': '654321','error_msg':'账号或密码错误'},
    {'name': '登录功能-异常登录-用户名错误', 'username': '34567890', 'password': 'lqh18276366','error_msg':'用户不存在'},
]
