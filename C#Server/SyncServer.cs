using System;  
using System.Net;  
using System.Net.Sockets;  
using System.Text;  
using System.Threading;

public class SynchronousSocketListener {  
  
    // Incoming data from the client.  
    public static string data = null;  
  
    public static void SendMessage(string msg, Socket handler){
        handler.Send(Encoding.ASCII.GetBytes(msg));
        Console.WriteLine( "Text Sent : {0}", msg);  
    }
    
    public static void StartListening() {  
        // Data buffer for incoming data.  
        // byte[] bytes = new Byte[1024];  
  
        // Establish the local endpoint for the socket.  
        // Dns.GetHostName returns the name of the
        // host running the application.  
        IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());  
        IPAddress ipAddress = ipHostInfo.AddressList[0];  
        IPEndPoint localEndPoint = new IPEndPoint(ipAddress, 11000);  
  
        // Create a TCP/IP socket.  
        Socket listener = new Socket(ipAddress.AddressFamily,  
            SocketType.Stream, ProtocolType.Tcp );  
  
        // Bind the socket to the local endpoint and
        // listen for incoming connections.  
        try {  
            listener.Bind(localEndPoint);  
            listener.Listen(10);  
  
            // Start listening for connections.  
            while (true) {  
                Console.WriteLine("Waiting for a connection...");  
                // Program is suspended while waiting for an incoming connection.  
                Socket handler = listener.Accept();  
                data = null;  
  
                // An incoming connection needs to be processed.  
                while (true) {  
                    string[] cmd = {"1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4"};
                    foreach (string s in cmd)
                    {
                        SendMessage(s, handler);
                        Thread.Sleep(100);
                    }
                    
                }  
                // handler.Shutdown(SocketShutdown.Both);  
                // handler.Close();  
            }  
  
        } catch (Exception e) {  
            Console.WriteLine(e.ToString());  
        }  
  
        Console.WriteLine("\nPress ENTER to continue...");  
        Console.Read();  
  
    }  
  
    public static int Main(String[] args) {  
        StartListening();  
        return 0;  
    }  
}