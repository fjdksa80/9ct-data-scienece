# Computing Technology Assessment Task 2 - Data Science
### Fraser Maple

## Identifying and Defining

### Mind map
![Mind map](./images/mind%20map.png)

### Hypothesis

**Artificial intelligence is eliminationg more jobs than it is creating.**

### Requirements Outline

**Functional Requirements**

- I need to be able to load my .csv file with my dataset.

- I need to be able to sort through my dataset to view specific relevant data points.

- I need to be able to create relevant and insightful charts with my data using matplotlib.

- The program will need to output a visualisation of the data or a filtered version of the dataset. My data will need to be stored in a .csv file. 

**Non-Functional Requirements**

- The user interface should be simple and easy to understand and use.

- The data should remain unchanged and shouldn't be modified by the user.

**Use Case**

Actor: User

Goal: To access and interact with existing data through the program’s user interface.

Preconditions:

- The dataset is already in the system.
- The user has access to the system interface.

Main Flow:

- User opens program and sees a text-based user interface.
- User selects one of four options:
    - View dataset
    - View visualisation
    - Filter data
    - Exit

- System does the selected action.

Postconditions:

- User has viewed/filtered data
- Data remains unchanged

## Researching and Planning

### Researching

While artificial intelligence is automating many tasks that were once done by humans, it also creates many new job opportunities. AI has the power to completely eliminate the need for humans in many tasks and jobs, and it's becoming clear that eventually all jobs will be affected if not completely replaced by artificial intelligence. However, AI also has the power to create job opportunities. For example, jobs in AI engineering, AI ethics, and AI training. But will these new jobs be enough to replace all those that it has taken?

Articles used:

https://www.theguardian.com/business/2025/aug/14/ai-artificial-intelligence-jobs-cleaning-construction-hospitality-australian-report
https://builtin.com/artificial-intelligence/ai-replacing-jobs-creating-jobs

### Data Dictionary

I have only included columns of data that are relevant to my hypothesis.
Field | Datatype | Format for display | Description | Example | Validation
|-|-|-|-|-|-|
|Year| integer | NNNN | Year the data was collected | 2018 | Must be a four digit number |
| Estimated Jobs Eliminated by AI (millions) | integer | NN...NN | Estimated number of jobs that have been elimated by AI | 10 | May have any number of digits, but must only contain numbers. |
| Estimated New Jobs Created by AI (millions) | integer | NN...NN | Estimated number of jobs that have been created by AI | 5 | May have any number of digits, but must only contain numbers.

## Testing and Evaluating

### Analyse and Conclude

Through analysis of my data, I have concluded that artificial intelligence is indeed taking more jobs than it is creating. This is to be expected as AI seems to be influencing and replacing jobs in all areas, while only creating jobs in a few specific areas. It is clear that artificial intelligence will be sure to radicalise the workplace in coming years, through creation, destruction, and augmentation of various jobs.

### Peer Verification

**Evaluation by Charles McDonagh**

**Plus:**

- Reasonably easy to navigate UI

- Small but refined dataset for quick processing

- Easy to explain graph with clear markings

**Minus:**

- Filtering system doesn't provide what should be entered (e.g. filtering by year doesn't have anything to say you should respond with yes or no)

- Filtering system by column is difficult to understand for someone without experience, leading to a poor UX.

**Implication:**

The UX is overall positive, and the program accomplishes the majority of it's goals, but its pretty clear that some elements still need refinement, especially the filtering.

### Evaluation

**Requirements Outline:**

My system checks all of the boxes laid out by my requirements outline. It allows for viewing and filtering of the dataset, as well as viewing of visualisations of the data through a simple user interface.

**Peer Feedback:**

All of the feedback that was provided for my system is understandable and expected. I could have improved some aspects that were pointed out if I had more time.

**Project Management:**

I could have better managed my time, and used my class time more effectively so that I would have to do less work at home, and have an overall more polished system. However, I did steadily work on it over the course of the past few weeks' lessons.

**Data Vailidity:**

I somewhat doubt the vailidity of my data for various reasons. The "estimated jobs eliminated by AI" claims to be in millions, and yet the data points were percentages. I removed the percentages from the data, assuming it to be a mistake, and to actually be a number in millions. However, the same data points also increase perfectly linearly over time, leading to further questions about my data's validity.

**User Experience:**

When filtering my dataset by column using my user interface, you are required to put in the column's number, rather than its name. If I had more time, I could have made it so that you could input the column's name in order to filter it, leading to an overall better user expierience.