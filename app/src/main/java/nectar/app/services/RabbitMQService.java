package nectar.app.services;

import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import nectar.app.config.RabbitMQConfig;

@Service
public class RabbitMQService {
    
    private RabbitTemplate rabbitTemplate;

    @Autowired
    private RabbitMQConfig rabbitMQConfig;

    @Autowired
    public RabbitMQService(RabbitTemplate rabbitTemplate) {
        this.rabbitTemplate = rabbitTemplate;
    }

    public void sendToDiscoverQueue(Object payload){
        this.rabbitTemplate.convertAndSend(rabbitMQConfig.getExperimentQueue(), payload);
    }
}
