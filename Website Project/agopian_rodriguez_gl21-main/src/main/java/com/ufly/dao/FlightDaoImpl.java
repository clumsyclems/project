/**
 * 
 */
package com.ufly.dao;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import javax.jdo.PersistenceManager;
import javax.jdo.PersistenceManagerFactory;
import javax.jdo.Query;
import javax.jdo.Transaction;
import javax.jdo.annotations.PersistenceCapable;

import com.ufly.Booking;
import com.ufly.Flight;
import com.ufly.ws.FlightWS;

/**
 * @author Paul
 *
 */

@PersistenceCapable
public class FlightDaoImpl implements FlightDao {

	
	PersistenceManagerFactory pmf;
	
	public FlightDaoImpl(PersistenceManagerFactory pmf) {
		this.pmf=pmf;
	}	
	
	public List<Flight> getFlightsFromCriteria(FlightWS.SearchCriteria sc) {

		PersistenceManager pm;
		Transaction tx;
		List<Flight> flights = new ArrayList<Flight>(); 
		
		
		// retrieve
		pm = pmf.getPersistenceManager();
		tx = pm.currentTransaction();
		// retainValues pour que les attributs soit gard?s
	    tx.setRetainValues(true);
		try {
			tx.begin();
			Query q = pm.newQuery(Flight.class);
			flights = (List<Flight>) q.execute();

			//System.out.println(sc.plane+sc.price+sc.destination+sc.seats);
			
			flights=flights.stream()
					
					.filter(p->p.getDepartureAirdrome().toUpperCase().contains(sc.departure.toUpperCase()))
				
					.filter(p->{
						switch(sc.price)
						{
							case "inf_50":
								return p.getPricePerPassenger() < 50;
							case "between_50_100":
								return (p.getPricePerPassenger() > 50 && p.getPricePerPassenger() < 100);
							case "between_100_150":
								return (p.getPricePerPassenger() > 100 && p.getPricePerPassenger() < 150);
							case "between_150_200":
								return (p.getPricePerPassenger() > 150 && p.getPricePerPassenger() < 200);
							case "sup_200":
								return (p.getPricePerPassenger() > 200);
							default:
								return true;
						}
						
					})
					
					.filter(p->{
						if(!sc.plane.toUpperCase().equals("ALL"))
							return (p.getAircraftModel().toUpperCase().equals(sc.plane.toUpperCase()));
						return true;
					})
					
					.filter(p->{
						if(!sc.destination.toUpperCase().equals("ALL"))
							return (p.getDestinationAirdrome().toUpperCase().contains(sc.destination.toUpperCase()));
						return true;
					})
					
					// we don't display flights for which there is no available seats
					.filter(p->p.getAvailableSeats()>=sc.seats && p.getAvailableSeats()>0)
				
					.filter(p->{
						if(sc.depDate!=null && !sc.depDate.equals("")) {
							System.out.println(sc.depDate);
							DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
							return LocalDateTime.parse(p.getDepartureDate(),formatter).toLocalDate().compareTo(LocalDate.parse(sc.depDate))==0;
						}
						return true;
					})					 
					
					.collect(Collectors.toList());
					
			tx.commit();
		} 

		finally {
			if (tx.isActive()) {
				tx.rollback();
			}

			pm.close();
			
		}
		
		
		for(Flight fget:flights) {
			System.out.println(fget.getFlightImg());
			System.out.println("flight retrieved : " + fget.getFlightDescription());
		}
		
		
		return flights ;

	}

	public Flight getInfoFromAFlight(long idFlight) {
		
		PersistenceManager pm;
		Transaction tx;
		Flight f;
// retrieve
		pm = pmf.getPersistenceManager();
		tx = pm.currentTransaction();
		// retainValues pour que les attributs soit gard?s
	    tx.setRetainValues(true);
		try {
			tx.begin();
			f = pm.getObjectById(Flight.class, idFlight);
			tx.commit();
			
		} 
		
		finally {
			if (tx.isActive()) {
				tx.rollback();
			}

			pm.close();
			
		}
		
		return f;
	}

	public void deleteAFlight(long idFlight) {
		
		PersistenceManager pm;
		Transaction tx;
		Flight f;

// retrieve
		pm = pmf.getPersistenceManager();
		tx = pm.currentTransaction();
	    	    
		try {
			tx.begin();
			f = pm.getObjectById(Flight.class, idFlight);
			pm.deletePersistent(f);
			tx.commit();
			
		} 
		
		finally {
			if (tx.isActive()) {
				tx.rollback();
			}

			pm.close();
			
		}
		
		System.out.println("The flight with the Id :"+idFlight+" has been deleted");// TODO Auto-generated method stub
		
	
	}

	public void sendReminderEmail(long idFlight) {
		System.out.println("The Reminder Email was sent for flight :"+idFlight);

	}
	
	public List<Flight> getAllFlights(){
		
		
		PersistenceManager pm;
		Transaction tx;
		Flight f;
		List<Flight> flist;
		
		// retrieve
		pm = pmf.getPersistenceManager();
		tx = pm.currentTransaction();
		// retainValues pour que les attributs soit gard?s
	    tx.setRetainValues(true);
		try {
			tx.begin();
			Query q = pm.newQuery(Flight.class);
			flist = (List<Flight>) q.execute();

			tx.commit();
			
		} 
		
		finally {
			if (tx.isActive()) {
				tx.rollback();
			}

			pm.close();
			
		}
		
		return flist;
		
	}

}
