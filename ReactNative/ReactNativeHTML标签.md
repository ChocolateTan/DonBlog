---
title: ReactNative HTML
date: 2018-10-02 09:09:09
categories: ReactNative
---
```js
var MyComponent = React.createClass({
  handleClick: function() {
    this.refs.myTextInput.focus();
  },
  render: function() {
    return (
      <div>
        <input type="text" ref="myTextInput" />
        <input type="button" value="Focus the text input" onClick={this.handleClick} />
      </div>
    );
  }
});
```

http://www.ruanyifeng.com/blog/2015/03/react.html

http://blog.csdn.net/guojin08/article/details/53126493

