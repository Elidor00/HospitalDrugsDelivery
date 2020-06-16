DOMAIN DRUG_DELIVERY
{	
	TEMPORAL_MODULE temporal_module = [0, 480], 500;

	PAR_TYPE EnumerationParameterType room = {Magazine, Room0, Room1, Room2, Room3};
	PAR_TYPE EnumerationParameterType patient = {Patient0, Patient1};	
	
	COMP_TYPE SingletonStateVariable MissionTimelineType (
		Idle(), Deliver(room, patient), At(room)
	)
	{
		VALUE Idle() [1, +INF]
		MEETS 
		{
			Deliver(?room, ?patient);
			At(?room);
		}
		
		VALUE Deliver(?room, ?patient) [1, +INF]
		MEETS
		{
			Idle();
		}
		
		VALUE At(?room) [1, +INF]
		MEETS 
		{
			Idle();
		}
	}
		
	COMP_TYPE SingletonStateVariable RobotMoveToRoom (
		GoingTo(room), At(room)
	)
	{
		VALUE At(?x1) [1, +INF]
		MEETS 
		{
			GoingTo(?x2);
		}
		
		VALUE GoingTo(?x1) [1, 30]
		MEETS 
		{
			At(?x2);
			?x1 = ?x2;
		}
	}
	
	COMP_TYPE SingletonStateVariable RobotDeliveryToPatient (
		Idle(), MoveTo(room, patient), Stop(room, patient) 
	)
	{		
		VALUE MoveTo(?roomX, ?patientX) [1, 2]
		MEETS 
		{
			Stop(?roomY, ?patientY);
			
			?roomX = ?roomY;
			?patientX = ?patientY;
		}
		
		VALUE Stop(?roomX, ?patientX) [1, 4]
		MEETS 
		{
			Idle();
			MoveTo(?room, ?patient);
		}
		
		VALUE Idle() [1, +INF] 
		MEETS 
		{
			MoveTo(?room, ?patient);
		}
		
	}
	
	COMP_TYPE SingletonStateVariable ComponentDeliver (
		Idle(), Deliver(room, patient) 
	)
	{
		VALUE Idle() [1, +INF]
		MEETS 
		{
			Deliver(?room, ?patient);
		}

		VALUE Deliver(?room, ?patient) [1, 1]
		MEETS 
		{
			Idle();
		}
	}
	
		
	COMPONENT RobotMoveToRoom {FLEXIBLE robot_move_to_room(trex_external)} : RobotMoveToRoom;	
	COMPONENT RobotDeliveryToPatient {FLEXIBLE robot_delivery(trex_external)} : RobotDeliveryToPatient;	
	COMPONENT ComponentDeliver {FLEXIBLE component_deliver(trex_external)} : ComponentDeliver;
	COMPONENT MissionTimeline {FLEXIBLE mission_timeline(functional)}: MissionTimelineType;
	
	SYNCHRONIZE RobotDeliveryToPatient.robot_delivery {
		VALUE Idle() {
			cd1 RobotMoveToRoom.robot_move_to_room.GoingTo(?roomX);
			cd2 ComponentDeliver.component_deliver.Idle();
			
			//EQUALS cd1;
			DURING [0,+INF] [0,+INF] cd2;
		}
		
		VALUE MoveTo(?roomX, ?patientX) {
			cd1 ComponentDeliver.component_deliver.Idle();
			cd2 RobotMoveToRoom.robot_move_to_room.GoingTo(?roomY);
			
			AFTER [0, +INF] cd2;
			DURING [0,+INF] [0,+INF] cd1;
			
			?roomX = ?roomY;
		}
		
		VALUE Stop(?roomX, ?patientX) {
			cd1 ComponentDeliver.component_deliver.Deliver(?roomY, ?patientY);
			EQUALS cd1;			
			?patientX = ?patientY;
			?roomX = ?roomY;
		}
	}
		
	SYNCHRONIZE RobotMoveToRoom.robot_move_to_room {
		
		VALUE At(?roomX) {
			cd1 RobotDeliveryToPatient.robot_delivery.MoveTo(?roomY, ?patientY);
			cd2 RobotDeliveryToPatient.robot_delivery.Stop(?roomW, ?patientW);
			
			CONTAINS [0,+INF] [0,+INF] cd1;
			CONTAINS [0,+INF] [0,+INF] cd2;
			
			?roomX = ?roomY;
			?patientY = ?patientW;
			?roomW = ?roomX;
		}
		
		VALUE GoingTo(?roomX) {
			cd1 ComponentDeliver.component_deliver.Idle();					
			DURING [0,+INF] [0,+INF] cd1;
		}		
	}	
			
	SYNCHRONIZE MissionTimeline.mission_timeline {
	
		VALUE  Deliver(?roomX, ?patientX) {
			
			cd5 ComponentDeliver.component_deliver.Deliver(?roomA, ?patientB);
			cd1 RobotMoveToRoom.robot_move_to_room.GoingTo(?roomY);
			cd2 RobotMoveToRoom.robot_move_to_room.At(?roomW);
			cd3 RobotDeliveryToPatient.robot_delivery.Stop(?roomZ, ?patientZ);
			
			cd5 AFTER [0, +INF] cd1;
			cd5 DURING [0, +INF][0, +INF] cd2;
			cd5 DURING [0, +INF][0, +INF] cd3;
			
			?roomX = ?roomA;
			?patientX = ?patientB;
			
			?roomA = ?roomY;
			?roomY = ?roomW;
			?roomW = ?roomZ;
			?patientB = ?patientZ;
			
		}			
	}
	
}
	
	
	
	