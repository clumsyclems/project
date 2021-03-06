package com.ufly.dao;

import java.util.List;

import com.ufly.Flight;
import com.ufly.ws.FlightWS;

public interface FlightDao {


	/**
	 * get a list of flights based on certain criteria
	 * GET
	 */
	List<Flight> getFlightsFromCriteria(FlightWS.SearchCriteria sc);

	
	/**
	 * get all the flights from the database
	 * 
	 */
	List<Flight> getAllFlights();

	
	/**
	 * get infos from a specific flight (with the id)
	 * GET
	 */
	Flight getInfoFromAFlight(long flightID);


	
	/**
	 * delete a specific flight
	 * DELETE
	 */
	void deleteAFlight(long flightID);

	/**
	 * Send an email to all the passengers concerned by the flight given by the id
	 * 
	 */
	void sendReminderEmail(long flightID);
}
