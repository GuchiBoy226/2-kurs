package com.company;

import javax.sound.sampled.*;
import javax.swing.*;

public class test extends JFrame {
    public static Audio a_bul;
    public test(){
        Clip clipSound;
        setTitle("КОСМОСОПИЗДЕЛОВКА");
        setResizable(false);
        a_bul=new Audio("musa.wav",0.7);
        test.a_bul.play();
        test.a_bul.setVolume();
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setSize(800,600);
        setLocation(400,400);
        add(new GameField());
        setVisible(true);
    }
    public static void main(String[] args){
        test testokno=new test();
    }
}
