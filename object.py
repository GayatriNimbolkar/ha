



public class helloworld {
    public static void applyDiscount(book_c[]books)
    {
        for(Books_c b:books)
            
            
        {b.Price_c*=0.9;}
    }
    

}




trigger hellowordTrigger on book__c (before insert) {

Book__c[] books=Trigger.new;
helloworld.applyDiscount(books);

}

