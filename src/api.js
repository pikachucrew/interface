import axios from 'axios'

export const getData = async () => {
  const data = await axios.get('https://pikacrew-be-test.herokuapp.com/yo')
  // console.log(data, 'data')
  return data
}

export const makeInt = ({ expressions }) => {
  return Object.keys(expressions).reduce((returnObj, expression) => {
    returnObj[expression] = Math.floor(expressions[expression] * 100)
    return returnObj
  }, {})
}

export const postData = async (expressions) => {
  console.log(2, expressions)
  const addedData = await axios.post('https://pikacrew-be-test.herokuapp.com/yo', expressions)
  return addedData;
}