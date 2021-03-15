package com.company;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.io.File;

import static java.lang.Thread.*;

public class GameField extends JPanel implements ActionListener {
    private static Audio spank;
    private static Audio billy;
    private Image player;
    private Image bg;
    private Image bily;
    private Image bot;
    private Image bullet;
    private int playerx = 400;
    private int playerY = 450;
    private int playerspeed = 10;
    private Timer timer;
    private boolean game = true;
    private boolean left = false;
    private boolean right = false;
    private boolean up = false;
    private boolean down = false;
    private boolean shoot = false;
    private boolean popal = false;
    private int bulletx = -30;
    private int bullety = -30;
    private int speedbullet = 15;
    private int chislo = 0;
    private int botx = 200;
    private int boty = 30;
    private int botspeed = 7;
    private int levANDright = 1;
    private int bothp = 20;
    private int ochko=0;
    private String strbot = "vrag.png";
    private int provmusic=0;

    public GameField() {
        imageload();
        initGame();
        addKeyListener(new FieldKeyListener());
        setFocusable(true);
    }

    public void initGame() {
        timer = new Timer(25, this);
        timer.start();
    }

    public void imageload() {
        ImageIcon zagruzkaPlayer = new ImageIcon("pidor.png");
        player = zagruzkaPlayer.getImage();
        ImageIcon zagruzkaBullet = new ImageIcon("bullet.png");
        bullet = zagruzkaBullet.getImage();
        ImageIcon zagruzkaBota = new ImageIcon(strbot);
        bot = zagruzkaBota.getImage();
        ImageIcon zagruzkaBG = new ImageIcon("bg.jpg");
        bg = zagruzkaBG.getImage();
    }

    public void botmove() {
        if (bothp >= 3) {
                botx += botspeed * levANDright;
                if (botx >= 695) {
                    levANDright = -1;
                        boty+=20;

                } else if (botx <= 0) {
                    levANDright = 1;
                        boty+=20;
                }
            if (popal==true) {
                boty-=20;
                popal=false;
            }

        } else {
            if (bullety <= boty + 1000 && bullety >= 30 && bulletx + 6 >= botx + 11 && bulletx - 7 <= botx + 89) {
                if (bulletx + 6 >= botx + 11 && bulletx - 7 <= botx + 89) {
                    botx += botspeed * levANDright;
                    if (botx >= 600) {
                        levANDright = -1;
                        boty+=20;
                    } else if (botx <= 100) {
                        levANDright = 1;
                        boty+=20;
                    }
                    if (popal==true) {
                        boty -= 20;
                        popal = false;
                    }
                }
            }
        }
        if(botx>=300&&botx<=340){
            ImageIcon zagruzkaBota = new ImageIcon(strbot);
            bot = zagruzkaBota.getImage();
        }
    }

    public void move() {
        if (left) {
            if (playerx<=0){
                playerx=0;
            }
            playerx -= playerspeed;
        }
        if (right) {
            if (playerx>=686){
                playerx=686;
            }
            playerx += playerspeed;
        }
        if (up) {
            if (playerY<=350){
                playerY=350;
            }
            playerY -= playerspeed;
        }
        if (down) {
            if (playerY>=465) {
                playerY=465;
            }
            playerY += playerspeed;
        }
        if (shoot == true) {
            if (bullety >= -30) {
                bullety -= speedbullet;
                if (bullety <= boty + 16 && bullety >= 30 && bulletx + 6 >= botx + 11 && bulletx - 7 <= botx + 89) {
                    bulletx = -30;
                    bullety = -30;
                    shoot = false;
                    botspeed++;
                    bothp--;
                    ochko++;
                    popal=true;
                    chislo = 0;
                    ImageIcon zagruzkaBota = new ImageIcon("spank1.png");
                    bot = zagruzkaBota.getImage();
                    spank=new Audio("spank.wav",0.7);
                    GameField.spank.play();
                    GameField.spank.setVolume();
                }
            } else {
                shoot = false;
                chislo = 0;
            }
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (game) {
            g.drawImage(bg, 0, 0, this);
            g.drawImage(player, playerx, playerY, this);
            g.drawImage(bot, botx, boty, this);
            g.drawImage(bullet, bulletx, bullety, this);
        }
        else{
            ImageIcon zagruzkaBG = new ImageIcon("bg.jpg");
            bg = zagruzkaBG.getImage();
            g.drawImage(bg, 0, 0, this);
            ImageIcon zagruzkaBilly = new ImageIcon("bag.png");
            bily= zagruzkaBilly.getImage();
            g.drawImage(bily, 100, 0, this);
            billy=new Audio("gg.wav",0.7);
            if (provmusic!=1) {
                GameField.billy.play();
                GameField.billy.setVolume();
            }
            provmusic=1;
        }
    }


    @Override
    public void actionPerformed(ActionEvent e) {
        repaint();
        move();
        botmove();
        if (bothp<=0){game=false;System.out.println("GOOD GAME="+ochko);}
        if (boty>=playerY-100){
            game=false;
            test.a_bul.stop();
            System.out.println("GAME OVER="+ochko);
        }
    }

    class FieldKeyListener extends KeyAdapter {
        @Override
        public void keyPressed(KeyEvent e) {
            if (e.getKeyCode() == KeyEvent.VK_LEFT) left = true;
            if (e.getKeyCode() == KeyEvent.VK_RIGHT) right = true;
            if (e.getKeyCode() == KeyEvent.VK_UP) up = true;
            if (e.getKeyCode() == KeyEvent.VK_DOWN) down = true;
            if (e.getKeyCode() == KeyEvent.VK_SPACE) shoot = true;
        }

        @Override
        public void keyReleased(KeyEvent e) {
            if (e.getKeyCode() == KeyEvent.VK_LEFT) left = false;
            if (e.getKeyCode() == KeyEvent.VK_RIGHT) right = false;
            if (e.getKeyCode() == KeyEvent.VK_UP) up = false;
            if (e.getKeyCode() == KeyEvent.VK_DOWN) down = false;
            if (e.getKeyCode() == KeyEvent.VK_SPACE) {
                chislo++;
                if (chislo == 1) {
                    shoot = true;
                    bulletx = playerx + 40;
                    bullety = playerY - 30;
                }
            }
        }
    }
}


