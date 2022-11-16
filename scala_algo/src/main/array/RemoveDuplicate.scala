package main.array
// leetcode-26. 删除有序数组中的重复项

object RemoveDuplicate {
  def removeDuplicate(nums: Array[Int]): Int = {
    var p = 0;
    var q = 1;
    while (q < nums.length) {
      if (nums(p) != nums(q)) {
        if (q - p > 1) {
          nums(p + 1) = nums(q)
        }
        p += 1;
      }
      q += 1;
    }
    return p + 1
  }

  def main(args: Array[String]) = {
    val nums = Array(1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 7) //这种方法实现了apply
    val k = removeDuplicate(nums)
    println(k, nums.slice(0, k).toBuffer)
  }

}
