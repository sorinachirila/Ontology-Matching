# Ontology-Matching
Study: DBpedia and Wikidata

# Scenario:
DBPedia and Wikidata are Linked Open Data projects, and at first sight it seems that they are very similar, but in fact they have absolutely different approaches to deal with structured data. DBPedia extracts data from the infoboxes in Wikipedia, while Wikidata is more like Wikipedia for data—its primary source of information are users. Wikipedia itself replaces old infoboxes by Wikidata, so DBPedia could use Wikidata as a data provider and editing interface. But there is a problem of heterogeneity. Both projects use different tools and knowledge, and it leads to usage of different names for the same concepts (terminological heterogeneity). And it’s important to accurately wire up those concepts in ontologies of projects. One of the principles of Linked Data: “Include links to other URIs, so that they can discover more things.”

The goal of the project is to create a system that maps items and properties of Wikidata to classes and properties of DBPedia.

Here is an example for properties, that is location
 - https://www.wikidata.org/wiki/Property:P276
 - http://dbpedia.org/ontology/location

Here is an example for items and classes , that is Berlin
 - https://www.wikidata.org/wiki/Q64
 - http://dbpedia.org/page/Berlin

 
Steps to follow for Berlin:
1. Run a SPARQl Query, against DBpedia Virtuoso endpoint, to get all owl:sameAs resources and select from there, the one from Wikidata

PREFIX owl:<http://www.w3.org/2002/07/owl#>

SELECT ?obj WHERE {
    dbpedia:Berlin (owl:sameAs|^owl:sameAs)* ?obj
}
 
2. Implement a class Course with the following private fields
 - int id
 - String name
 - add constructors (default, with all arguments), getters and setters
 - override equals and hashCode as Course will be part of a Set
 
3. Implement a class <Teacher> with the following private fields
 - int id 
 - String name
 - Set Course courses (will be a HashSet)
 - add constructors (default, with all arguments), getters and setters
 - override equals and hashCode as Course will be part of a Set
 - add following methods: 
   - Set <Course> getCourses()
   - Course getCourse(int id)
   - setCourses (Set<Course>)
   - addCourser(Course)
   - updateCourse(Course)
   - removeCourse(Course)
4. Implement a class <Group> with the following private fields
 - int id
 - String name
 - Set Teacher teachers (will be a HashSet)
 - Set Student students (will be a HashSet)
 - add constructors (default, with all arguments), getters and setters
 - override equals and hashCode as <Group> will be part of a Set
 - add following methods;
   - Set <Teacher> getTeachers()
   - Teacher getTeacher(int id)
   - setTeachers (Set <Teacher>)
   - addTeacher(Teacher)
   - updateTeacher(Teacher, String teacherName)
   - removeTeacher(Teacher)
   - Set <Student> getStudents()
   - Student getStudent(int id)
   - setStudents (Set <Student>)
   - addStudent(Student)
   - updateStudent(Student, String studentName)
   - removeStudent(Student)
5. Implement a class Application with the following private fields 
  - Set Group groups (will be a HashSet)
  - add a main method where you should add 2 Groups to the set of groups 
  - each Group should have 4 Teachers
  - each Group should have 3 Students
  - each Teacher should teach 2 Courses
  - display information for all the groups in a friendly format 

Question: why is better to store Teachers for example in a Set and not in a List?

