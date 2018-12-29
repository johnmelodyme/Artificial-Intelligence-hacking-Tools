/*Chabot Name: [ Sabrina ]
	<!-- Copyright © 2018-2019 John Melody All Rights Reserved

              _       _             __  __      _           _       
            | |     | |           |  \/  |    | |         | |      
            | | ___ | |__  _ __   | \  / | ___| | ___   __| |_   _ 
        _   | |/ _ \| '_ \| '_ \  | |\/| |/ _ \ |/ _ \ / _` | | | |
       | |__| | (_) | | | | | | | | |  | |  __/ | (_) | (_| | |_| |     v1.1.2  
        \____/ \___/|_| |_|_| |_| |_|  |_|\___|_|\___/ \__,_|\__, |
                                                              __/ |
                                                             |___/
*/

import java.awt.event.ActionListener;
import javax.swing.JFrame;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class sabrinabot extends JFrame {
	
	//serial
	private static final long serialVersionUID = -8479855412126432205L;

	//Input Setting
	private JTextField txtEnter = new JTextField();
	
	//chat area:
	private JTextArea txtChat = new JTextArea();
	
	public sabrinabot() {
		//Frame Attrib:
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setSize(600 , 600);
		this.setVisible(true);
		this.setResizable(false);
		this.setLayout(null);
		this.setTitle("Sabrina");
		
		//txtenter attrib:
		txtEnter.setLocation(5 ,5);
		txtEnter.setSize(590 ,30);
		
		//Action event::txtenter:
		txtEnter.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent arg0) {
				String uText = txtEnter.getText();
				txtChat.append("User: " + uText + "\n");
				
				if(uText.contains("hi")){
					sabrinaSay("Hello There.");
				}
				else {
					int decider = (int) Math.random()*3+1;
					if(decider == 1) {
						sabrinaSay("Please Rephrase that.");
					}
					else if (decider == 3) {
						sabrinaSay("what?");
				}
			}
				txtEnter.setText("");
		}
	}
		
		
		//txtChat attrib:
		txtChat.setLocation(2, 0);
		txtChat.setSize(400, 400);
		txtChat.setEditable(false);
		
		//Add to frame:
		this.add(txtEnter);
		this.add(txtChat);
		
	}
	
	public void sabrinaSay(String s) {
		txtChat.append("Sabrina: " + s + "\n");
	}
	
	public static void main(String[] args) {
		
	}
	
}
