// ```1) ```
// https://www.codewars.com/kata/563089b9b7be03472d00002b/train/javascript

Array.prototype.remove_ = function(integer_list, values_list) {
  let result = [];
  for (let i = 0; i < integer_list.length; i++) {
    let element = integer_list[i];
    if (values_list.includes(element) === false) {
      result.push(element);
    }
  }
  return result;
};



