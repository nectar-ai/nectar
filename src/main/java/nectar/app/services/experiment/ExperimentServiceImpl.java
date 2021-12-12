package nectar.app.services.experiment;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import nectar.app.models.Experiment;
import nectar.app.repositories.ExperimentRespository;
import nectar.app.services.RabbitMQService;

@Service
public class ExperimentServiceImpl implements ExperimentService {

    @Autowired
    private RabbitMQService rabbitMQService;

    @Autowired
    private ExperimentRespository experimentRespository;
    
    @Override
    public Experiment executeExperiment(Experiment experiment, boolean rerun) {
        if(!rerun) {
            this.experimentRespository.save(experiment);
        }
        this.rabbitMQService.sendToDiscoverQueue(experiment);
        return experiment;
    }

    @Override
    public List<Experiment> findAllExperiments() {
        return this.experimentRespository.findAll();
    }
}
