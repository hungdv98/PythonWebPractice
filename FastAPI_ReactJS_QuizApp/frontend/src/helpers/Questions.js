var exams;

fetch("/gexam/1")
.then(res => res.json())
.then(data => {
    console.log(data)
    exams = data 
})
.catch((err) => console.log(err));

// export const Questions = exams;

export const Questions = [
    {
      "id": 1,
      "question_name": "1 + 1 = ",
      "opt1": "9",
      "opt2": "4",
      "opt3": "2",
      "opt4": "11"
    },
    {
      "id": 2,
      "question_name": "2 + 1 = ",
      "opt1": "9",
      "opt2": "3",
      "opt3": "2",
      "opt4": "11"
    },
    {
      "id": 3,
      "question_name": "11 + 1 = ",
      "opt1": "9",
      "opt2": "4",
      "opt3": "2",
      "opt4": "12"
    },
    {
      "id": 4,
      "question_name": "11 + 12 = ",
      "opt1": "9",
      "opt2": "23",
      "opt3": "2",
      "opt4": "11"
    },
    {
      "id": 5,
      "question_name": "10 + 1 = ",
      "opt1": "9",
      "opt2": "4",
      "opt3": "2",
      "opt4": "11"
    },
    {
      "id": 6,
      "question_name": "5 + 1 = ",
      "opt1": "6",
      "opt2": "4",
      "opt3": "2",
      "opt4": "11"
    },
    {
      "id": 7,
      "question_name": "1 + 3 = ",
      "opt1": "9",
      "opt2": "4",
      "opt3": "2",
      "opt4": "11"
    },
    {
      "id": 8,
      "question_name": "16 + 1 = ",
      "opt1": "17",
      "opt2": "4",
      "opt3": "2",
      "opt4": "11"
    },
    {
      "id": 9,
      "question_name": "1 + 15 = ",
      "opt1": "9",
      "opt2": "16",
      "opt3": "2",
      "opt4": "11"
    },
    {
      "id": 10,
      "question_name": "1 + 0 = ",
      "opt1": "9",
      "opt2": "4",
      "opt3": "1",
      "opt4": "11"
    }
  ]