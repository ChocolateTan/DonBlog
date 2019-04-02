---
title: Laravel
date: 2018-10-02 09:09:09
categories: php
---
### 路由参数

參數按照順序與名稱無關

```php
Route::get('posts/{post}/comments/{comment}', function ($postId, $commentId) {
    //
});
```

### 可選參數

```php
Route::get('user/{name?}', function ($name = null) {
    return $name;
});

Route::get('user/{name?}', function ($name = 'John') {
    return $name;
});
```



