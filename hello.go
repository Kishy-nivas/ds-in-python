package main 

import (
"encoding/json"
"fmt"
"github.com/gorilla/mux"
"net/http"
)

type API struct {
	Message string "json: message"
}

func Hello(w http.ResponseWriter ,r* http.Request){
	urlParams:=mux.Vars(r)
	name:=urlParams["user"]
	HelloMessage:"Hello," +name 
	message:=API{HelloMessage}
	output,err= json.Marshal(message)
	if err!=nil{
		fmt.Println("something went wrong")
	}
	fmt.Fprintf(w.string(output))
}

func main() {
	gorillaRoute :=mux.NewRouter() 
	goriallRoute.HandleFunc("/api/{user:[0-9]+}",Hello)
	http.Handle("/",goriallRoute)
	http.ListenAndServe(":8080",nil)
}
