DOMAIN DRUG_DELIVERY
{	
	TEMPORAL_MODULE temporal_module = [0, 480], 500; //1 unità = 15 secondi, 1 turno dura fino a 2 ore
	
	PAR_TYPE EnumerationParameterType room = {Warehouse, Room0, Room1, Room2, Room4, Room5, Room3, Room6, Room7, Room8};
	PAR_TYPE EnumerationParameterType patient = {Patient0, Patient1, Patient2};	
		
	COMP_TYPE SingletonStateVariable MissionTimelineSV (
		Idle(), Deliver(room, patient)
	)
	{
		VALUE Idle() [1, +INF]
		MEETS 
		{
			Deliver(?room, ?patient);
		}
		
		VALUE Deliver(?room, ?patient) [1, +INF]
		MEETS
		{
			Idle();
		}
	}
		
	COMP_TYPE SingletonStateVariable RobotMoveToRoomSV (
		GoingTo(room), At(room)
	)
	{
		VALUE At(?r1) [1, +INF]
		MEETS 
		{
			GoingTo(?r2);
		}
		
		VALUE GoingTo(?r1) [2, 8] // 30 s, 2 m
		MEETS 
		{
			At(?r2);
			?r2 = ?r1;
		}
	}
	
	COMP_TYPE SingletonStateVariable RobotDeliveryToPatientSV (
		Idle(), MoveTo(room, patient), Stop(room, patient) 
	)
	{		
		VALUE MoveTo(?roomX, ?patientX) [1, 3] // 15 sec 45 sec
		MEETS 
		{
			Stop(?roomY, ?patientY);
			
			?roomY = ?roomX;
			?patientY = ?patientX;
		}
		
		VALUE Stop(?roomX, ?patientX) [1, 4] // 15 sec 1 m
		MEETS 
		{
			Idle();
		}
		
		VALUE Idle() [1, +INF] 
		MEETS 
		{
			MoveTo(?room, ?patient);
		}
	}

	COMPONENT RobotDeliveryToPatient {FLEXIBLE robot_delivery(primitive)} : RobotDeliveryToPatientSV;
	COMPONENT RobotMoveToRoom {FLEXIBLE robot_move_to_room(primitive)} : RobotMoveToRoomSV;	
	COMPONENT MissionTimeline {FLEXIBLE mission_timeline(functional)}: MissionTimelineSV;


	
	SYNCHRONIZE MissionTimeline.mission_timeline {
	
		VALUE  Deliver(?roomX, ?patientX) {
			
			cd0 RobotMoveToRoom.robot_move_to_room.At(?room0);
			cd1 RobotDeliveryToPatient.robot_delivery.Stop(?room1, ?patient1);
			
			DURING [0, +INF] [0, +INF] cd0;
			CONTAINS [0, +INF] [0, +INF] cd1;
						

			?room0 = ?roomX;
			?room1 = ?roomX;
			?patient1 = ?patientX;
		}			
	}
	
	SYNCHRONIZE RobotDeliveryToPatient.robot_delivery
	{
		VALUE MoveTo(?r, ?p)
		{
			cd0 RobotMoveToRoom.robot_move_to_room.At(?r0);
			
			DURING [0, +INF] [0, +INF] cd0;
			
			?r0 = ?r;
		}
	}

}