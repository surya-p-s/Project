package com.example.marinesoft

import android.content.ContentValues
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.ProgressBar
import android.widget.Toast
import com.google.firebase.Timestamp
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.ktx.firestore
import com.google.firebase.ktx.Firebase

class DetailsPage : AppCompatActivity() {
    private lateinit var auth : FirebaseAuth
    private lateinit var fName : EditText
    private lateinit var lName : EditText
    private lateinit var pNumber : EditText
    private var db=Firebase.firestore
    private lateinit var email : EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_details_page)

        auth = Firebase.auth
        db = FirebaseFirestore.getInstance()
        email = findViewById(R.id.emailText3)
        fName = findViewById(R.id.firstName)
        lName = findViewById(R.id.lastName)
        pNumber = findViewById(R.id.phoneNumber)

        val submitButton = findViewById<Button>(R.id.submitButton)

        submitButton.setOnClickListener {
            val firstName = fName.text.toString().trim()
            val lastName = lName.text.toString().trim()
            val number = pNumber.text.toString().trim()
            val sEmail = email.text.toString().trim()

            val userDetails = hashMapOf(
                "FirstName" to firstName,
                "LastName" to lastName,
                "Phone Number" to number,
                "Date" to Timestamp.now(),
                "Email Id" to sEmail
            )
            val progressBar=findViewById<ProgressBar>(R.id.progressBar3)
            progressBar.visibility= View.VISIBLE

            db.collection("User Details").document(sEmail)
                .set(userDetails)
                .addOnCompleteListener {
                    Log.d(ContentValues.TAG,"Details Added Successfully")
                }
                .addOnFailureListener { e ->
                    Log.d(ContentValues.TAG, "Error adding document",e)}

            val intent = Intent(this, SignUpActivity::class.java)
            startActivity(intent)
        }

    }

}