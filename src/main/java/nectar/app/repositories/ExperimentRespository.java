package nectar.app.repositories;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import nectar.app.models.Experiment;

@Repository
public interface ExperimentRespository extends MongoRepository<Experiment, String> {
    
}
