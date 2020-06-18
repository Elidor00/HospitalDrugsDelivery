DOMAIN DRUG_DELIVERY
{	
	TEMPORAL_MODULE temporal_module = [0, 480], 500;

	PAR_TYPE EnumerationParameterType room = {Magazine, Room0, Room1, Room2, Room3};
	PAR_TYPE EnumerationParameterType patient = {Patient0, Patient1, Patient2};	
	
	COMP_TYPE SingletonStateVariable RobotMoveToRoom (
		GoingTo(room), At(room)
	)
	{
		VALUE At(?x1) [1, +INF]
		MEETS 
		{
			GoingTo(?x2);
			?x1 != ?x2;
		}
		
		VALUE GoingTo(?x1) [1, 30]
		MEETS 
		{
			At(?x2);
			?x1 = ?x2;
		}
	}
	
	COMP_TYPE SingletonStateVariable RobotDeliveryToPatient (
		MoveTo(room, patient), Deliver(room, patient) 
	)
	{		
		VALUE MoveTo(?roomX, ?patientX) [1, +INF]
		MEETS 
		{
			Deliver(?roomY, ?patientY);
			
			?roomX = ?roomY;
			?patientX = ?patientY;
		}
		
		VALUE Deliver(?roomX, ?patientX) [1, 4]
		MEETS 
		{
			MoveTo(?roomY, ?patientY);
			?patientX != ?patientY;
		}
				
	}

	COMPONENT RobotMoveToRoom {FLEXIBLE robot_move_to_room(trex_internal)} : RobotMoveToRoom;	
	COMPONENT RobotDeliveryToPatient {FLEXIBLE robot_delivery(trex_internal)} : RobotDeliveryToPatient;	
	
	SYNCHRONIZE RobotDeliveryToPatient.robot_delivery {
		
		VALUE Deliver(?roomX, ?patientX) {
			cd1 RobotMoveToRoom.robot_move_to_room.At(?roomY);
			DURING [0,+INF] [0,+INF] cd1;			
			?roomX = ?roomY;
		}	
	}
	
	SYNCHRONIZE RobotMoveToRoom.robot_move_to_room {
		
		VALUE GoingTo(?roomX) {
			cd1 RobotDeliveryToPatient.robot_delivery.MoveTo(?roomY, ?patientY);
			
			DURING [0, +INF] [0, +INF] cd1;
			?roomX = ?roomY;
		}
	}	
}