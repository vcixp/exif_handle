package org.vcixp.task;


import cn.hutool.core.date.DateUtil;
import cn.hutool.core.io.FileUtil;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.io.File;
import java.util.List;

@Component
public class FileDeleteTask {
    @Value("${app.location}")
    private String location;
    @Scheduled(cron = "0 0 1 ? * *")
    public void executeTask() {
        List<File> files = FileUtil.loopFiles(location);
        for (File file : files) {
            if(!file.getName().startsWith(DateUtil.today() + "_")){
                FileUtil.del(file);
            }
        }
    }

}
