# HospitalDrugsDelivery

## Introduction


## Development Environment
You need to install:
- Webots R2020a Revision 1 ([site](https://cyberbotics.com/) or [github repo](https://github.com/cyberbotics/webots))
- PLATINUm ([github repo](https://github.com/pstlab/PLATINUm))

Follow this [guide](https://cyberbotics.com/doc/guide/using-your-ide#pycharm) to set PyCharm as an external IDE for Webots

### Programming language
- Python 3.8.2

## Execution
1.  Clone project
    ```
    git clone https://github.com/Elidor00/HospitalDrugsDelivery.git
    ```  
2. Open scenario ``` HospitalDrugsDelivery/worlds/Hospital.wbt ``` in Webots
3. Launch ```pioneer3dx_controller.py``` inside ```HospitalDrugsDelivery/controllers/main_controller/```
4. Run the simulation in webots

N.B. By default the simulation is started using the file ```plan.txt``` as a plan


## Create your customized plan

- Launch PLATINUm as a Maven Project on Eclipse IDE
- Create a domains folder for a problem
- Create a new ```.ddl``` and ```.pdl``` file or modify an existing one 
- Run ```main``` class in ```it.istc.pst.platinum.testing.app.deliberative.PlatinumPlannerTester``` specifying the full path of the ```.ddl``` and ```.pdl`` files 
- Copy the output file into the folder ```HospitalDrugsDelivery```
- Follow steps 3 and 4 of the previous section
