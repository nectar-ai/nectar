package nectar.app.services.experiment;

import java.util.List;

import nectar.app.models.Experiment;

public interface ExperimentService {
    
    public List<Experiment> findAllExperiments();
    public Experiment executeExperiment(Experiment experiment, boolean rerun);
}
