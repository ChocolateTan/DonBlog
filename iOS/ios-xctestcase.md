# iOS XCTestCase

| 函数 | 用途 |
| :-----| :----- |
| setUp | 继承与XCTestCase 函数测试文件开始执行的时候运行 |
| tearDown | 继承与XCTestCase 测试函数运行完之后执行 |
| testExample | 测试的例子函数 |
| testPerformanceExample | 性能测试 |


XCTest的测试范围

* （1）基本逻辑测试处理测试
* （2）异步加载数据测试
* （3）数据mock测试

```swift
import XCTest
@testable import test
 
class testTests: XCTestCase {
 
    override func setUp() {
        super.setUp()
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }
 
    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }
 
    func testExample() {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
    }
 
    func testPerformanceExample() {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }
 
}
```

```swift
//异步
import XCTest
import Alamofire
 
@testable import test
 
class NetworkAsyncTests: XCTestCase {
 
    override func setUp() {
        super.setUp()
    }
 
    override func tearDown() {
        super.tearDown()
    }
 
    func testAsynNetworkTest() {
        let networkExpection = expectation(description: "networkDownSuccess")
        Alamofire.request("http://www.httpbin.org/get?key=Xctest", method: .get, parameters: nil, encoding: JSONEncoding.default).responseJSON { (respons) in
            XCTAssertNotNil(respons)
            networkExpection.fulfill()
            }
        
        //设置XCWaiter等待期望时间，只是细节不同。
//        waitForExpectations(timeout: 0.00000001)
//        wait(for: [networkExpection], timeout: 0.00000001)
 
            
        //XCTWaiter.Result  枚举类型如下
        /*
        public enum Result : Int {
            
            
            case completed
            
            case timedOut
            
            case incorrectOrder
            
            case invertedFulfillment
            
            case interrupted
        }
        */
        let result = XCTWaiter(delegate: self).wait(for: [networkExpection], timeout:  1)
        if result == .timedOut {
            print("超时")
        }
        
    }
 
    func testPerformanceExample() {
        
        self.measure {
           
        }
    }
 
}
```