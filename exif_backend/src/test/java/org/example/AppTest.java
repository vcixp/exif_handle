package org.example;


import cn.hutool.core.date.DateUtil;
import cn.hutool.core.io.FileUtil;

import java.io.File;
import java.util.List;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    public static void main(String[] args) {
        List<File> files = FileUtil.loopFiles("/home/ycx/workspaces/test");
        for (File file : files) {
            if(!file.getName().startsWith(DateUtil.today() + "_")){
                FileUtil.del(file);
            }
        }
    }
}
