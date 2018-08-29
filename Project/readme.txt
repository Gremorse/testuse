用户user -- 微信号，手机，头像，昵称，角色(买家/代练)，擅长
用户订单user_order -- 订单编号，下单人，下单时间，订单信息(继续细化)，状态，金额，资料证实，接单人
用户订单状态变化seq_user_order -- 订单编号，状态顺序，状态，发生时间，发生对象
订单状态定义dict_order_status -- 编号，序号，状态名称
用户订单交流信息order_chat -- 订单编号，下单人，接单人，发言对象，发言内容，发言时间
段位价格关系dict_business_payment -- 价格编号，段位起始，段位结束，段位星数，单价

pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support