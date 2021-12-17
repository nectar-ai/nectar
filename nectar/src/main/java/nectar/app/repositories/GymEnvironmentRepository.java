package nectar.app.repositories;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import nectar.app.models.GymEnvironment;

@Repository
public interface GymEnvironmentRepository extends MongoRepository<GymEnvironment, String> {
    
}
