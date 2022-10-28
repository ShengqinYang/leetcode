package test

import main.sc_array.ArrayDemo

object ArrayTest {
  def main(args: Array[String]): Unit = {
    val demo = new ArrayDemo(10)
    demo.insert(0, '零')
    demo.insert(1, '一')
    demo.insert(2, '贰')
    demo.insert(3, '叁')
    demo.insert(4, '肆')
    demo.append(value = '路')
    demo.append(value = '1')
    demo.append(value = '2')
    demo.append(value = '3')
    demo.append(value = '3')
//    assert(demo.append(value = '3'))

    for (i <- 0 until demo.length) {
      println(i, demo.find(i))
    }
//    println(demo.find(3))
//    demo.delete(1)
//    println(demo.find(1))

//    println(demo.find(-1))

  }

}
