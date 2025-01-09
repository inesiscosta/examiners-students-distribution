document.addEventListener("DOMContentLoaded", () => {
  const students = JSON.parse(localStorage.getItem("students")) || [];
  const examiners = JSON.parse(localStorage.getItem("examiners")) || [];
  const constraints = JSON.parse(localStorage.getItem("constraints")) || {};

  const assignmentsDiv = document.getElementById("assignments");
  const workloadDiv = document.getElementById("workload");
  const randomizeButton = document.getElementById("randomizeButton");

  const assignExaminers = () => {
    const assignments = {};
    const supervisorWorkload = {};

    // Initialize workloads
    examiners.forEach((examiner) => {
      supervisorWorkload[examiner] = 0;
    });

    students.forEach((student) => {
      // Determine eligible supervisors for the student
      const eligibleExaminers = examiners.filter(
        (examiner) => !constraints[examiner] || !constraints[examiner].includes(student)
      );

      // Randomly assign two eligible supervisors
      const assigned = eligibleExaminers.sort(
        (a, b) => supervisorWorkload[a] - supervisorWorkload[b]
      ).slice(0, 2);

      assignments[student] = assigned;

      // Update workloads
      assigned.forEach((examiner) => {
        supervisorWorkload[examiner]++;
      });
    });

    return { assignments, supervisorWorkload };
  };

  const displayResults = (assignments, workload) => {
    assignmentsDiv.innerHTML = "<h2>Lista Alunos:</h2>";
    workloadDiv.innerHTML = "<h2>Número de Alunos por Avaliador:</h2>";

    // Display assignments
    const assignmentList = Object.keys(assignments).map(
      (student) => `<p>${student}: ${assignments[student].join(", ")}</p>`
    ).join("");
    assignmentsDiv.innerHTML += assignmentList;

    // Display workloads
    const workloadList = Object.keys(workload).map(
      (examiner) => `<p>${examiner}: ${workload[examiner]}</p>`
    ).join("");
    workloadDiv.innerHTML += workloadList;
  };

  // Initial assignments
  let { assignments, supervisorWorkload } = assignExaminers();
  displayResults(assignments, supervisorWorkload);

  // Re-Randomize functionality
  randomizeButton.addEventListener("click", () => {
    const result = assignExaminers();
    assignments = result.assignments;
    supervisorWorkload = result.supervisorWorkload;
    displayResults(assignments, supervisorWorkload);
  });
});