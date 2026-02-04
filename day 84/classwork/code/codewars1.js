// https://www.codewars.com/kata/52fba2a9adcd10b34300094c/train/javascript

function transpose(matrix) {
  let result = [];

  for (let i = 0; i < matrix[0].length; i++) {
    result[i] = []; 

    for (let mat = 0; mat < matrix.length; mat++) {
      result[i][mat] = matrix[mat][i];
    }
  }

  return result;
}
