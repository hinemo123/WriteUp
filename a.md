## Debug file war
Step 1: Create project

![image](https://user-images.githubusercontent.com/54855855/136367265-49ae4d53-7a00-4f7a-a7b6-46ef30cae9cf.png)

Step 2: Name the project

![image](https://user-images.githubusercontent.com/54855855/136367414-370819b2-6748-4032-a4b3-5b9d1f166bc5.png)

Step 3: Choose Add Configuration -> '+' -> Tomcat Server -> Local

![image](https://user-images.githubusercontent.com/54855855/136367817-03705db8-6d66-47c7-92ab-2eee9d7334b7.png)

Step 4: Download Tomcat and add to Application server

[Download Tomcat](http://tomcat.apache.org/)

- In the Server / Application server section, select the tomcat installation directory.

![image](https://user-images.githubusercontent.com/54855855/136369171-c1238b57-abff-45c9-be49-4c5a0f1124d8.png)

Step 5: Add file war to Deployment

![image](https://user-images.githubusercontent.com/54855855/136368369-38291043-b804-4daf-a081-bbf4d600ab1c.png)

Step 6: Setup remote debugging

- In the Startup/Connection -> Environment variables

Add 
```
Name = JAVA_OPTS
Value = -agentlib:jdwp=transport=dt_socket,address=127.0.0.1:5005,suspend=n,server=y
```
![image](https://user-images.githubusercontent.com/54855855/136411338-fecbf4ac-2714-4bca-a534-2229748720c6.png)

Step 7: Unzip file war to get lib

Run-on the terminal in the directory containing the file war

`jar -xvf ./filename.war`

![image](https://user-images.githubusercontent.com/54855855/136414029-0cba2808-b5c6-422c-8fa1-27430194f9df.png)

Step 8: Copy all unzip source to folder src

![image](https://user-images.githubusercontent.com/54855855/136415266-e694df00-7313-4be7-87a2-41c64f5e9503.png)

Step 9: Add all jar files in WEB-INF\lib folder to lib in our project

- Select File -> Project Structure then select Libraries -> '+' -> java, and select all jar files in WEB-INF\lib

- Ctrl+Alt+Shift+S

![image](https://user-images.githubusercontent.com/54855855/136417246-98795e47-5965-4e01-a2d3-17b8de5b090e.png)

Final Step: Run program

- Run `Shift+F10`

![image](https://user-images.githubusercontent.com/54855855/136421434-e1979851-f37c-4be2-9b6e-53b0da1672eb.png)

In Edit Configuarations

![image](https://user-images.githubusercontent.com/54855855/136421737-efe77d73-364e-4225-9a89-554e2909cb20.png)

Copy url at `URl` and access
