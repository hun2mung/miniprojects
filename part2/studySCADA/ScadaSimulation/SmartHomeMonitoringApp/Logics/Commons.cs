using uPLibrary.Networking.M2Mqtt;

namespace SmartHomeMonitoringApp.Logics
{
    internal class Commons
    {
        public static string BROKERHOST { get; set; } = "127.0.0.1";  // localhost

        public static string MQTTTOPIC { get; set; } = "SmartHome/IoTData/";

        public static string MYSQL_CONNSTRING { get; set; } = "Server=localhost;" +
                                                                "Port=3306;" +
                                                                "Database=miniproject;" +
                                                                "Uid=root;" +
                                                                "Pwd=12345;";
        public static MqttClient MQTT_CLIENT {get; set;}
    }
}
