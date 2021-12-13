package nectar.app.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import nectar.app.models.Experiment;
import nectar.app.services.experiment.ExperimentService;

@RestController
@RequestMapping("/api/v1/experiments")
public class ExperimentController {
    
    @Autowired
    private ExperimentService experimentService;

    @GetMapping("/")
    public List<Experiment> findAllExperiments() {
        return this.experimentService.findAllExperiments();
    }

    @PostMapping(value = {"/"})
    public Experiment executeExperiment(@RequestBody Experiment experiment,
        @RequestParam boolean rerun) {
        return this.experimentService.executeExperiment(experiment, rerun);
    }
}
