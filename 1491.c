double average(int* salary, int salarySize){
    int min_salary = INT_MAX;
    int max_salary = INT_MIN;
    int total_salary = 0;
    for (int i = 0; i < salarySize; i++) {
        if (salary[i] < min_salary) min_salary = salary[i];
        if (salary[i] > max_salary) max_salary = salary[i];
        total_salary += salary[i];
    }
    total_salary -= min_salary + max_salary;
    int num_employees = salarySize - 2;
    return (double) total_salary / num_employees;
}