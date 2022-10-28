package main.sc_array

class ArrayDemo(capactiy: Int) {

  var data: Array[Char] = new Array[Char](capactiy)
  var length: Int = 0

  def find(index: Int): Char = {
    if (index < 0 || index > length) {
      //      return null
      return 0.toChar
    }
    data(index)

  }

  def insert(index: Int, value: Char): Boolean = {
    if (length == capactiy) {
      return false
    }
    if (index < 0 || index >= capactiy) {
      return false
    }
    //从索引length开倒序检索，直到i-1 = index 的时候停下
    for (i <- length until index by -1) {
      data(i) = data(i - 1)
    }
    data(index) = value
    length += 1
    true
  }

  def delete(index: Int): Char = {
    if (length == 0) {
      throw new IllegalStateException("array is empty")
    }
    if (index > length) {
      throw new IllegalStateException("index out of range,current data lenght is " + length)
    }
    val result = data(index)
    for (i <- index until length - 1) {
      data(i) = data(i + 1)
    }
    length -= 1
    result
  }

  //  追加写，数组末尾追加一个
  def append(value: Char): Boolean = {
    if (length == capactiy) {
      throw new IllegalStateException("capactiy is full,current data lenght is " + length)
    }
    data(length) = value
    length += 1
    true
  }

  def print: String = {
    //    data.subSequence(0, length).toString
    data.toString
  }

}
