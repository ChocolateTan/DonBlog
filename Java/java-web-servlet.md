# java web servlet

learn java web
类型 Servlet、GenericServlet、HttpServlet
Servlet 生命周期
 * 1.实例化（使用构造方法创建对象）
 * 2.初始化  执行init方法 当Servlet第一次被创建对象时执行该方法,该方法在整个生命周期中只执行一次
 * 3.服务     执行service方法 对客户端响应的方法,该方法会被执行多次，每次请求该servlet都会执行该方法
 * 4.销毁    执行destroy方法 当Servlet被销毁时执行该方法

destory 方法被调用后，servlet 被销毁，但是并没有立即被回收，再次请求时，并没有重新初始化。

private String message;

@Override
public void init() throws ServletException {
    message = "Hello World , Nect To Meet You: " + System.currentTimeMillis();
    System.out.println("servlet初始化……");
    super.init();
}

@Override
public void doGet(HttpServletRequest req, HttpServletResponse response) throws ServletException, IOException {
    response.setContentType("text/html");
    PrintWriter writer = response.getWriter();
    writer.write("<h1>" + message + "</h1>");
    destroy();
}

@Override
public void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    // TODO Auto-generated method stub
    super.doPost(req, resp);
}

@Override
public void destroy() {
    System.out.println("servlet销毁！");
    super.destroy();
}
servlet初始化……
servlet销毁！
2017-7-6 19:48:52 org.apache.catalina.core.StandardContext reload
信息: Reloading Context with name [/myServlet] has started
servlet销毁！
2017-7-6 19:48:52 org.apache.catalina.core.StandardContext reload
信息: Reloading Context with name [/myServlet] is completed
servlet初始化……
servlet销毁！
servlet销毁！
servlet销毁！
servlet销毁！
servlet销毁！
servlet销毁！
servlet销毁！
