var exams;

fetch("/gexam/1")
.then(res => res.json())
.then(data => {
    console.log(data)
    exams = data 
})
.catch((err) => console.log(err));

export const Questions = exams;