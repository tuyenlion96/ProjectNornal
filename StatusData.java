public class StatusData 
{
    boolean isCheck;
    int[] iAge = {18, 19, 20, 21, 22};
    String sUserName;
    String sPasswd;
    String sFirstName;
    String sLastName;

    // Constructure
    StatusData()
    {
        sUserName = "tuyenlion96";
        sPasswd = "Hang250599";
        sFirstName = "";
        sLastName = "";
    }

    public void saveUserData(StatusData dat)
    {
        sFirstName = dat.sFirstName;
        sLastName = dat.sLastName;
        sUserName = dat.sUserName;
        sPasswd = dat.sPasswd;
    }

    public void getUserData() throws InterruptedException
    {
        
        for (int i = 0; i <= 10; i++)
        {
            System.out.println("Loging %d" + i*10);
            Thread.sleep(1000);
        }
    }

    public boolean checkingEntryApplication(int iUserAge )
    {
        String sOutConsl = "";
        for (int i: iAge)
        {
            if (iUserAge == i)
            {
                isCheck = true;
                sOutConsl = "You're old user in my system";
                break;
            }
        }

        if (isCheck == false)
        {
            sOutConsl = "You're new user in my system";
        }

        System.out.println(sOutConsl);

        return isCheck;
    }
}
